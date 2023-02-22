# @markdown Prompts
author = 'random' #@param ['random', 'Lisa Frank', 'Manasse Rampino', 'maya hayuk', 'ron english wynwood', 'Dimitri Sirenko', 'iannocent', 'Beo88', 'kiradiron', 'MAD DOG JONES', 'kenny scharf'] {allow-input: true}
colorfulTags = 'neon blue bright' #@param ['random', 'bright', 'flashy', 'gaudy', 'multicolored', 'hued', 'rich', 'splashy', 'vibrant', 'vivid', 'kaleidoscopic', 'prismatic', 'loud', 'chromatic', 'colorful', 'fluorescent', 'neon', 'fantastic', 'multicolor', 'eye-catching', 'amazing', 'pretty', 'funny'] {allow-input: true}
things = 'space cars cats' #@param ['random', 'Fantasy world ', 'nature', 'love', 'party', 'animals', 'world', 'planets', 'robots', 'space', 'planets', 'paint splash', 'fireworks', 'party', 'nature', 'robots', 'people', 'fruits', 'birds', 'pets', 'puppies', 'kittens'] {allow-input: true}

#@markdown

#@markdown Video parameters
import random
videos = 1#@param {type:"number"}

for i in range(videos):
    colorfulTags_list = ['bright', 'flashy', 'gaudy', 'multicolored', 'hued', 'rich', 'splashy', 'vibrant', 'vivid', 'kaleidoscopic', 'prismatic', 'loud', 'chromatic', 'colorful', 'fluorescent', 'neon', 'fantastic', 'multicolor', 'eye-catching', 'amazing', 'pretty', 'funny']
    authors_list = ['Lisa Frank', 'Manasse Rampino', 'maya hayuk', 'ron english wynwood', 'Dimitri Sirenko', 'iannocent', 'Beo88', 'kiradiron', 'MAD DOG JONES', 'kenny scharf']
    things_list = ['Fantasy world ', 'nature', 'love', 'party', 'animals', 'world', 'planets', 'robots', 'space', 'planets', 'paint splash', 'fireworks', 'party', 'nature', 'robots', 'people', 'fruits', 'birds', 'pets', 'puppies', 'kittens']

    if author == 'random':
        author = random.choice(authors_list)

    if colorfulTags == 'random':
        colorfulTags = random.choice(colorfulTags_list) + ' ' + random.choice(colorfulTags_list)

    if things == 'random':
        things = random.choice(things_list) + ' ' + random.choice(things_list) + ' ' + random.choice(things_list)

    ans = f'0:({author} {colorfulTags} {things} : 1)'

    width = None
    height = None

    format = 'square' #@param ['square', 'horizontal', 'vertical']
    if format == 'square':
        width = 400
        height = 400
    elif format == 'horizontal':
        width = 400
        height = 225
    elif format == 'vertical':
        width = 225
        height = 400

    trajectory = 'random' #@param ['random', 'spiral']

    text_prompts = ans
    model = "vqgan_imagenet_f16_16384"
    interval =  1
    initial_image = ""
    target_images = ""
    seed = -1

    fps = 12 #@param {type: 'integer'}

    seconds = 4 #@param {type: 'integer'}
    max_frames = fps * seconds

    showing_images = True #@param {type: 'boolean'}
    iterations_per_frame = "0: (25)"#@param {type:"string"}

    #@markdown

    #@markdown Upscaling video

    #@markdown resolutions:
    _HD = True #@param {type:"boolean"}
    _FullHD = True #@param {type:"boolean"}
    _2K = False #@param {type:"boolean"}
    _4K = False #@param {type:"boolean"}

    resolutions = []
    algorithms = []

    if _HD:
        resolutions.append([720, 1280])
    if _FullHD:
        resolutions.append([1080, 1920])
    if _2K:
        resolutions.append([1440, 2560])
    if _4K:
        resolutions.append([2160, 3840])

    #@markdown algorithms:

    soft = True #@param {type: "boolean"}
    medium = True #@param {type: "boolean"}
    hard = False #@param {type: "boolean"}

    if soft:
        algorithms.append('srmd_ncnn_vulkan')
    if medium:
        algorithms.append('waifu2x_ncnn_vulkan')
    if hard:
        algorithms.append('realsr_ncnn_vulkan')

    key_frames = True
    if trajectory == 'random':
        ra1 = round(random.uniform(-5.0,5.0), 5)
        ra2 = round(random.uniform(-5.0,5.0), 5)
        ra3 = round(random.uniform(-5.0,5.0), 5)
        ra4 = round(random.uniform(-5.0,5.0), 5)
        ra5 = round(random.uniform(-5.0,5.0), 5)

        rz1 = round(random.uniform(0.925,1.1), 5)
        rz2 = round(random.uniform(0.925,1.1), 5)
        rz3 = round(random.uniform(0.925,1.1), 5)
        rz4 = round(random.uniform(0.925,1.1), 5)
        rz5 = round(random.uniform(0.925,1.1), 5)

        rtx1 = round(random.uniform(-30.0,30.0), 5)
        rtx2 = round(random.uniform(-30.0,30.0), 5)
        rtx3 = round(random.uniform(-30.0,30.0), 5)
        rtx4 = round(random.uniform(-30.0,30.0), 5)
        rtx5 = round(random.uniform(-30.0,30.0), 5)
        rtx6 = round(random.uniform(-30.0,30.0), 5)
        rtx7 = round(random.uniform(-30.0,30.0), 5)
        rtx8 = round(random.uniform(-30.0,30.0), 5)

        rty1 = round(random.uniform(-25.0,25.0), 5)
        rty2 = round(random.uniform(-25.0,25.0), 5)
        rty3 = round(random.uniform(-25.0,25.0), 5)
        rty4 = round(random.uniform(-25.0,25.0), 5)
        rty5 = round(random.uniform(-25.0,25.0), 5)
        rty6 = round(random.uniform(-25.0,25.0), 5)
        rty7 = round(random.uniform(-25.0,25.0), 5)
        rty8 = round(random.uniform(-25.0,25.0), 5)

    elif trajectory == 'spiral':
        ra1 = round(random.uniform(4.0,4.0), 5)
        ra2 = round(random.uniform(4.0,4.0), 5)
        ra3 = round(random.uniform(4.0,4.0), 5)
        ra4 = round(random.uniform(4.0,4.0), 5)
        ra5 = round(random.uniform(4.0,4.0), 5)

    rz1 = 0.96
    rz2 = 0.96
    rz3 = 0.96
    rz4 = 0.96
    rz5 = 0.96

    rtx1 = rtx2 = rtx3 = rtx4 = rtx5 = rtx6 = rtx7 = rtx8 = round(random.uniform(-9.0,9.0), 5)

    rty1 = rty2 = rty3 = rty4 = rty5 = rty6 = rty7 = rty8 = round(random.uniform(-9.0,9.0), 5)

    angle = f"0:({ra1}), 60:({ra2}), 120:({ra3}), 180:({ra4}), 240:({ra4}), 300:({ra5})"
    zoom = f"0:({rz1}), 60:({rz2}), 135:({rz3}), 210:({rz4}), 285:({rz5}))"
    translation_x = f"0:({rtx1}), 45:({rtx2}), 90:({rtx2}), 135:({rtx2}), 180:({rtx2}), 225:({rtx2}), 270:({rtx2}), 315:({rtx2})"
    translation_y = f"0:({rty1}), 45:({rty1}), 90:({rty1}), 135:({rty1}), 180:({rty1}), 225:({rty1}), 270:({rty1}), 315:({rty1})"

    save_all_iterations = False
    if initial_image != "":
        print(
          "WARNING: You have specified an initial image. Note that the image resolution "
          "will be inherited from this image, not whatever width and height you specified. "
          "If the initial image resolution is too high, this can result in out of memory errors."
        )
    elif width * height > 160000:
        print("Внимание: очень высокое разрешение. Может не хватить видеопамяти.")
    model_names={
        "vqgan_imagenet_f16_16384": 'ImageNet 16384',
        "vqgan_imagenet_f16_1024":"ImageNet 1024", 
        "wikiart_1024":"WikiArt 1024",
        "wikiart_16384":"WikiArt 16384",
        "coco":"COCO-Stuff",
        "faceshq":"FacesHQ",
        "sflckr":"S-FLCKR"
    }
    model_name = model_names[model]

    if seed == -1:
        seed = None

    def parse_key_frames(string, prompt_parser=None):
        import re
        pattern = r'((?P<frame>[0-9]+):[\s]*[\(](?P<param>[\S\s]*?)[\)])'
        frames = dict()
        for match_object in re.finditer(pattern, string):
            frame = int(match_object.groupdict()['frame'])
            param = match_object.groupdict()['param']
            if prompt_parser:
                frames[frame] = prompt_parser(param)
            else:
                frames[frame] = param

        if frames == {} and len(string) != 0:
            raise RuntimeError('Key Frame string not correctly formatted')
        return frames

    def get_inbetweens(key_frames, integer=False):
        key_frame_series = pd.Series([np.nan for a in range(max_frames)])
        for i, value in key_frames.items():
            key_frame_series[i] = value
        key_frame_series = key_frame_series.astype(float)
        key_frame_series = key_frame_series.interpolate(limit_direction='both')
        if integer:
            return key_frame_series.astype(int)
        return key_frame_series

    def split_key_frame_text_prompts(frames):
        prompt_dict = dict()
        for i, parameters in frames.items():
            prompts = parameters.split('|')
            for prompt in prompts:
                string, value = prompt.split(':')
                string = string.strip()
                value = float(value.strip())
                if string in prompt_dict:
                    prompt_dict[string][i] = value
                else:
                    prompt_dict[string] = {i: value}
        prompt_series_dict = dict()
        for prompt, values in prompt_dict.items():
            value_string = (
                ', '.join([f'{value}: ({values[value]})' for value in values])
            )
            prompt_series = get_inbetweens(parse_key_frames(value_string))
            prompt_series_dict[prompt] = prompt_series
            prompt_list = []
            for i in range(max_frames):
            prompt_list.append(
                ' | '.join(
                    [f'{prompt}: {prompt_series_dict[prompt][i]}'
                   for prompt in prompt_series_dict]
                )
            )
        return prompt_list

    if key_frames:
        try:
            text_prompts_series = split_key_frame_text_prompts(
                parse_key_frames(text_prompts)
            )
        except RuntimeError as e:
            print(
              "WARNING: You have selected to use key frames, but you have not "
              "formatted `text_prompts` correctly for key frames.\n"
              "Attempting to interpret `text_prompts` as "
              f'"0: ({text_prompts}:1)"\n'
              "Please read the instructions to find out how to use key frames "
              "correctly.\n"
            )
            text_prompts = f"0: ({text_prompts}:1)"
            text_prompts_series = split_key_frame_text_prompts(
                parse_key_frames(text_prompts)
            )

        try:
            target_images_series = split_key_frame_text_prompts(
                parse_key_frames(target_images)
            )
        except RuntimeError as e:
            print(
                "WARNING: You have selected to use key frames, but you have not "
                "formatted `target_images` correctly for key frames.\n"
                "Attempting to interpret `target_images` as "
                f'"0: ({target_images}:1)"\n'
                "Please read the instructions to find out how to use key frames "
                "correctly.\n"
            )
            target_images = f"0: ({target_images}:1)"
            target_images_series = split_key_frame_text_prompts(
                parse_key_frames(target_images)
            )

            try:
                angle_series = get_inbetweens(parse_key_frames(angle))
            except RuntimeError as e:
                print(
                    "WARNING: You have selected to use key frames, but you have not "
                    "formatted `angle` correctly for key frames.\n"
                    "Attempting to interpret `angle` as "
                    f'"0: ({angle})"\n'
                    "Please read the instructions to find out how to use key frames "
                    "correctly.\n"
                )
                angle = f"0: ({angle})"
                angle_series = get_inbetweens(parse_key_frames(angle))

            try:
                zoom_series = get_inbetweens(parse_key_frames(zoom))
            except RuntimeError as e:
                print(
                    "WARNING: You have selected to use key frames, but you have not "
                    "formatted `zoom` correctly for key frames.\n"
                    "Attempting to interpret `zoom` as "
                    f'"0: ({zoom})"\n'
                    "Please read the instructions to find out how to use key frames "
                    "correctly.\n"
                )
                zoom = f"0: ({zoom})"
                zoom_series = get_inbetweens(parse_key_frames(zoom))

            try:
                translation_x_series = get_inbetweens(parse_key_frames(translation_x))
            except RuntimeError as e:
                print(
                    "WARNING: You have selected to use key frames, but you have not "
                    "formatted `translation_x` correctly for key frames.\n"
                    "Attempting to interpret `translation_x` as "
                    f'"0: ({translation_x})"\n'
                    "Please read the instructions to find out how to use key frames "
                    "correctly.\n"
                )
                translation_x = f"0: ({translation_x})"
                translation_x_series = get_inbetweens(parse_key_frames(translation_x))

            try:
                translation_y_series = get_inbetweens(parse_key_frames(translation_y))
            except RuntimeError as e:
            print(
                "WARNING: You have selected to use key frames, but you have not "
                "formatted `translation_y` correctly for key frames.\n"
                "Attempting to interpret `translation_y` as "
                f'"0: ({translation_y})"\n'
                "Please read the instructions to find out how to use key frames "
                "correctly.\n"
            )
            translation_y = f"0: ({translation_y})"
            translation_y_series = get_inbetweens(parse_key_frames(translation_y))

            try:
                iterations_per_frame_series = get_inbetweens(
                  parse_key_frames(iterations_per_frame), integer=True
                )
            except RuntimeError as e:
                print(
                    "WARNING: You have selected to use key frames, but you have not "
                    "formatted `iterations_per_frame` correctly for key frames.\n"
                    "Attempting to interpret `iterations_per_frame` as "
                    f'"0: ({iterations_per_frame})"\n'
                    "Please read the instructions to find out how to use key frames "
                    "correctly.\n"
                )
            iterations_per_frame = f"0: ({iterations_per_frame})"

            iterations_per_frame_series = get_inbetweens(
                parse_key_frames(iterations_per_frame), integer=True
            )
    else:
        text_prompts = [phrase.strip() for phrase in text_prompts.split("|")]
        if text_prompts == ['']:
            text_prompts = []
        if target_images == "None" or not target_images:
            target_images = []
        else:
            target_images = target_images.split("|")
            target_images = [image.strip() for image in target_images]

        angle = float(angle)
        zoom = float(zoom)
        translation_x = float(translation_x)
        translation_y = float(translation_y)
        iterations_per_frame = int(iterations_per_frame)

    args = argparse.Namespace(
        prompts=text_prompts,
        image_prompts=target_images,
        noise_prompt_seeds=[],
        noise_prompt_weights=[],
        size=[width, height],
        init_weight=0.,
        clip_model='ViT-B/32',
        vqgan_config=f'{model}.yaml',
        vqgan_checkpoint=f'{model}.ckpt',
        step_size=0.1,
        cutn=64,
        cut_pow=1.,
        display_freq=interval,
        seed=seed,
    )

    path = f'{working_dir}/steps'
    !rm -r {path}
    !mkdir --parents {path}


    if key_frames:
        filename = "video.mp4"
    else:
        filename = f"{'_'.join(text_prompts).replace(' ', '')}.mp4"
    filepath = f'{working_dir}/{filename}'


    if key_frames:
        filename = "video.mp4"
    else:
        filename = f"{'_'.join(text_prompts).replace(' ', '')}.mp4"
    filepath = f'{working_dir}/{filename}'

  # Delete memory from previous runs
  !nvidia-smi -caa
  for var in ['device', 'model', 'perceptor', 'z']:
    try:
        del globals()[var]
    except:
        pass

  try:
      import gc
      gc.collect()
  except:
      pass

  try:
      torch.cuda.empty_cache()
  except:
      pass

  device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
  print('Using device:', device)
  if not key_frames:
      if text_prompts:
          print('Using text prompts:', text_prompts)
      if target_images:
          print('Using image prompts:', target_images)
  if args.seed is None:
      seed = torch.seed()
  else:
      seed = args.seed
  torch.manual_seed(seed)
  print('Using seed:', seed)
  
  model = load_vqgan_model(args.vqgan_config, args.vqgan_checkpoint).to(device)
  perceptor = clip.load(args.clip_model, jit=False)[0].eval().requires_grad_(False).to(device)
  
  cut_size = perceptor.visual.input_resolution
  e_dim = model.quantize.e_dim
  f = 2**(model.decoder.num_resolutions - 1)
  make_cutouts = MakeCutouts(cut_size, args.cutn, cut_pow=args.cut_pow)
  n_toks = model.quantize.n_e
  toksX, toksY = args.size[0] // f, args.size[1] // f
  sideX, sideY = toksX * f, toksY * f
  z_min = model.quantize.embedding.weight.min(dim=0).values[None, :, None, None]
  z_max = model.quantize.embedding.weight.max(dim=0).values[None, :, None, None]
  stop_on_next_loop = False  # Make sure GPU memory doesn't get corrupted from cancelling the run mid-way through, allow a full frame to complete

  def read_image_workaround(path):
      """OpenCV reads images as BGR, Pillow saves them as RGB. Work around
      this incompatibility to avoid colour inversions."""
      im_tmp = cv2.imread(path)
      return cv2.cvtColor(im_tmp, cv2.COLOR_BGR2RGB)

  for i in range(max_frames):
      if stop_on_next_loop:
        break
      if key_frames:
          text_prompts = text_prompts_series[i]
          text_prompts = [phrase.strip() for phrase in text_prompts.split("|")]
          if text_prompts == ['']:
              text_prompts = []
          args.prompts = text_prompts

          target_images = target_images_series[i]

          if target_images == "None" or not target_images:
              target_images = []
          else:
              target_images = target_images.split("|")
              target_images = [image.strip() for image in target_images]
          args.image_prompts = target_images

          angle = angle_series[i]
          zoom = zoom_series[i]
          translation_x = translation_x_series[i]
          translation_x = -1 * translation_x
          translation_y = translation_y_series[i]
          iterations_per_frame = iterations_per_frame_series[i]
          print(
              f'text_prompts: {text_prompts}'
              f'angle: {angle}',
              f'zoom: {zoom}',
              f'translation_x: {translation_x}',
              f'translation_y: {translation_y}',
              f'iterations_per_frame: {iterations_per_frame}'
          )
      try:
          if i == 0 and initial_image != "":
              img_0 = read_image_workaround(initial_image)
              z, *_ = model.encode(TF.to_tensor(img_0).to(device).unsqueeze(0) * 2 - 1)
          elif i == 0 and not os.path.isfile(f'{working_dir}/steps/{i:04d}.png'):
              one_hot = F.one_hot(
                  torch.randint(n_toks, [toksY * toksX], device=device), n_toks
              ).float()
              z = one_hot @ model.quantize.embedding.weight
              z = z.view([-1, toksY, toksX, e_dim]).permute(0, 3, 1, 2)
          else:
              if save_all_iterations:
                  img_0 = read_image_workaround(
                      f'{working_dir}/steps/{i:04d}_{iterations_per_frame}.png')
              else:
                  img_0 = read_image_workaround(f'{working_dir}/steps/{i:04d}.png')

              center = (1*img_0.shape[1]//2, 1*img_0.shape[0]//2)
              trans_mat = np.float32(
                  [[1, 0, translation_x],
                  [0, 1, translation_y]]
              )
              rot_mat = cv2.getRotationMatrix2D( center, angle, zoom )

              trans_mat = np.vstack([trans_mat, [0,0,1]])
              rot_mat = np.vstack([rot_mat, [0,0,1]])
              transformation_matrix = np.matmul(rot_mat, trans_mat)

              img_0 = cv2.warpPerspective(
                  img_0,
                  transformation_matrix,
                  (img_0.shape[1], img_0.shape[0]),
                  borderMode=cv2.BORDER_WRAP
              )
              z, *_ = model.encode(TF.to_tensor(img_0).to(device).unsqueeze(0) * 2 - 1)
          i += 1

          z_orig = z.clone()
          z.requires_grad_(True)
          opt = optim.Adam([z], lr=args.step_size)

          normalize = transforms.Normalize(mean=[0.48145466, 0.4578275, 0.40821073],
                                          std=[0.26862954, 0.26130258, 0.27577711])

          pMs = []

          for prompt in args.prompts:
              txt, weight, stop = parse_prompt(prompt)
              embed = perceptor.encode_text(clip.tokenize(txt).to(device)).float()
              pMs.append(Prompt(embed, weight, stop).to(device))

          for prompt in args.image_prompts:
              path, weight, stop = parse_prompt(prompt)
              img = resize_image(Image.open(path).convert('RGB'), (sideX, sideY))
              batch = make_cutouts(TF.to_tensor(img).unsqueeze(0).to(device))
              embed = perceptor.encode_image(normalize(batch)).float()
              pMs.append(Prompt(embed, weight, stop).to(device))

          for seed, weight in zip(args.noise_prompt_seeds, args.noise_prompt_weights):
              gen = torch.Generator().manual_seed(seed)
              embed = torch.empty([1, perceptor.visual.output_dim]).normal_(generator=gen)
              pMs.append(Prompt(embed, weight).to(device))

          def synth(z):
              z_q = vector_quantize(z.movedim(1, 3), model.quantize.embedding.weight).movedim(3, 1)
              return clamp_with_grad(model.decode(z_q).add(1).div(2), 0, 1)

          def add_xmp_data(filename):
              imagen = ImgTag(filename=filename)
              imagen.xmp.append_array_item(libxmp.consts.XMP_NS_DC, 'creator', 'VQGAN+CLIP', {"prop_array_is_ordered":True, "prop_value_is_array":True})
              if args.prompts:
                  imagen.xmp.append_array_item(libxmp.consts.XMP_NS_DC, 'title', " | ".join(args.prompts), {"prop_array_is_ordered":True, "prop_value_is_array":True})
              else:
                  imagen.xmp.append_array_item(libxmp.consts.XMP_NS_DC, 'title', 'None', {"prop_array_is_ordered":True, "prop_value_is_array":True})
              imagen.xmp.append_array_item(libxmp.consts.XMP_NS_DC, 'i', str(i), {"prop_array_is_ordered":True, "prop_value_is_array":True})
              imagen.xmp.append_array_item(libxmp.consts.XMP_NS_DC, 'model', model_name, {"prop_array_is_ordered":True, "prop_value_is_array":True})
              imagen.xmp.append_array_item(libxmp.consts.XMP_NS_DC, 'seed',str(seed) , {"prop_array_is_ordered":True, "prop_value_is_array":True})
              imagen.close()

          def add_stegano_data(filename):
              data = {
                  "title": " | ".join(args.prompts) if args.prompts else None,
                  "notebook": "VQGAN+CLIP",
                  "i": i,
                  "model": model_name,
                  "seed": str(seed),
              }
              lsb.hide(filename, json.dumps(data)).save(filename)

          @torch.no_grad()
          def checkin(i, losses):
              losses_str = ', '.join(f'{loss.item():g}' for loss in losses)
              tqdm.write(f'i: {i}, loss: {sum(losses).item():g}, losses: {losses_str}')
              out = synth(z)
              TF.to_pil_image(out[0].cpu()).save('progress.png')
              add_stegano_data('progress.png')
              add_xmp_data('progress.png')
              if showing_images:
                display.display(display.Image('progress.png')) #Отвечвет за вывод картинки в консоль

          def save_output(i, img, suffix=None):
              filename = \
                  f"{working_dir}/steps/{i:04}{'_' + suffix if suffix else ''}.png"
              imageio.imwrite(filename, np.array(img))
              add_stegano_data(filename)
              add_xmp_data(filename)

          def ascend_txt(i, save=True, suffix=None):
              out = synth(z)
              iii = perceptor.encode_image(normalize(make_cutouts(out))).float()

              result = []

              if args.init_weight:
                  result.append(F.mse_loss(z, z_orig) * args.init_weight / 2)

              for prompt in pMs:
                  result.append(prompt(iii))
              img = np.array(out.mul(255).clamp(0, 255)[0].cpu().detach().numpy().astype(np.uint8))[:,:,:]
              img = np.transpose(img, (1, 2, 0))
              if save:
                  save_output(i, img, suffix=suffix)
              return result

          def train(i, save=True, suffix=None):
              opt.zero_grad()
              lossAll = ascend_txt(i, save=save, suffix=suffix)
              if i % args.display_freq == 0 and save:
                  checkin(i, lossAll)
              loss = sum(lossAll)
              loss.backward()
              opt.step()
              with torch.no_grad():
                  z.copy_(z.maximum(z_min).minimum(z_max))

          with tqdm() as pbar:
              if iterations_per_frame == 0:
                  save_output(i, img_0)
              j = 1
              while True:
                  suffix = (str(j) if save_all_iterations else None)
                  if j >= iterations_per_frame:
                      train(i, save=True, suffix=suffix)
                      break
                  if save_all_iterations:
                      train(i, save=True, suffix=suffix)
                  else:
                      train(i, save=False, suffix=suffix)
                  j += 1
                  pbar.update()
      except KeyboardInterrupt:
        stop_on_next_loop = True
        pass



  # import subprocess in case this cell is run without the above cells
  import subprocess
  import os

  init_frame = 1
  last_frame = i

  if (os.path.isdir('/drive/My Drive/Render_result/')):
    filepath = '/drive/My Drive/Render_result/video.mp4'
  elif (os.path.isdir('/drive/MyDrive/Render_result/')):
    filepath = '/drive/MyDrive/Render_result/video.mp4'
  else:
    raise ValueError('Директория гугл диска Render_result не обнаружена!')

  def uniquify(path):
      filename, extension = os.path.splitext(path)
      counter = 1

      while os.path.exists(path):
          path = filename + str(counter) + extension
          counter += 1

      return path

  filepath = uniquify(filepath)

  frames = []
  # tqdm.write('Generating video...')
  try:
      zoomed
  except NameError:
      image_path = f'{working_dir}/steps/%04d.png'
  else:
      image_path = f'{working_dir}/steps/zoomed_%04d.png'

  cmd = [
      'ffmpeg',
      '-y',
      '-vcodec',
      'png',
      '-r',
      str(fps),
      '-start_number',
      str(init_frame),
      '-i',
      image_path,
      '-c:v',
      'libx264',
      '-vf',
      f'fps={fps}',
      '-pix_fmt',
      'yuv420p',
      '-crf',
      '17',
      '-preset',
      'veryslow',
      filepath
  ]

  process = subprocess.Popen(cmd, cwd=f'{working_dir}/steps/', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  if process.returncode != 0:
      print(stderr)
      print(
          "Ошибка! Попробуйте понизить разрешение"
      )
      raise RuntimeError(stderr)
  else:
      print("Видео создано!")

  print("Начат апскейлинг...") 

  directory = '/content/drive/MyDrive/videos/Render_result'

  for alg in algorithms:
    for resol in resolutions:
      outPath = filepath + '_' + alg + '_' + str(resol[1]) + '_UPSCALED.mp4'

      if format == 'square':
        !python video2x-4.7.0/src/video2x.py -i '{filepath}' -o '{outPath}' -d '{alg}' -h '{resol[1]}'
      elif format == 'horizontal':
        !python video2x-4.7.0/src/video2x.py -i '{filepath}' -o '{outPath}' -d '{alg}' -h '{resol[1]}'
      elif format == 'vertical':
        !python video2x-4.7.0/src/video2x.py -i '{filepath}' -o '{outPath}' -d '{alg}' -h '{resol[0]}'

  print("Апскейлинг успешно завершен!") 

print(f'Сгенерировано {videos} видео!')